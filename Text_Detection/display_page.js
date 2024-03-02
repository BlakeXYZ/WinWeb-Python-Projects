const my_apiEndpoint = "./db/scanned_card_data.json";
const display_data = document.querySelector('#display-data');

const getData = async () => {
    const res = await fetch(my_apiEndpoint);

    if (!res.ok) {
        throw new Error(`HTTP error! status: ${res.status}`);
    }

    const data = await res.json();

    return data;
}

const displayData = async (data) => {
    let dataDisplay = data.map((object) => {
        const { name, usdPrice, rarity, urlLink, urlThumbnailImage, confidenceValue } = object;

        return `
            <div class="card-container">
                <img src="${urlThumbnailImage}" alt="${name} Thumbnail">
                <div class="text-container">
                    <p><strong>Name:</strong> ${name}</p>
                    <p><strong>USD Price:</strong> $${usdPrice}</p>
                    <p><strong>Rarity:</strong> ${rarity}</p>
                    <p><strong>Confidence Value:</strong> ${confidenceValue}</p>
                    <p><a href="${urlLink}" target="_blank"><strong>Scryfall URL Link</strong></a></p>
                </div>
            </div>
        `;
    }).join('');

    display_data.innerHTML = dataDisplay;
}

////////////////////////////////////////////////////////////////////                                          SORT DATA functions


const sortData = (data, key) => {

    // Define a mapping for rarity values
    const rarityOrder = {
        'common': 1,
        'uncommon': 2,
        'rare': 3,
        'mythic': 4
    };


    return data.slice().sort((a, b) => {

        // sort by A-Z
        if (key === 'name') {
            console.log("SORT string: a - z");
            return a[key].localeCompare(b[key]);

        // sort by custom rarity order
        } else if (key === 'rarity') {

            console.log("custom rarity order");
            const aOrder = rarityOrder[a[key]] || 0;
            const bOrder = rarityOrder[b[key]] || 0;

            return bOrder - aOrder;
        
        // sort by Price Num Value High -> Low
        } else if (key === 'usdPrice') {
            console.log("SORT price high to low");
            // Parse string to float
            const aValue = parseFloat(a[key]) || -Infinity; // Set to -Infinity if null
            const bValue = parseFloat(b[key]) || -Infinity; // Set to -Infinity if null

            return bValue - aValue;
        }

        // Add more conditions for other keys if needed
        // } else if (key === 'anotherKey') {
        //    // Handle sorting for another key
        // }

        // Default case: just return 0 for no change in order
        return 0;
    });
};


//////////////////////////////////////////////////////////////////////                                        HANDLE sort + search filter    


const handleSortOrSearchChange = async () => {

    const sortDropdown = document.getElementById('sort-dropdown');
    const selectedKey = sortDropdown.value;

    const searchString = document.getElementById('search-input').value.toLowerCase(); // Convert to lowercase for case-insensitive search

    const data = await getData();

    // Handle sorting
    if (selectedKey) {
        resultData = sortData(data, selectedKey);
        console.log(`Sorted Data (${selectedKey}):`, resultData);
    }

    // Handle searching
    if (searchString) {
        resultData = resultData.filter(item => item.name.toLowerCase().includes(searchString));
        console.log('Filtered Data:', resultData);
    }

    // Display the final result
    displayData(resultData || data);


}

//////////////////////////////////////////////////////////////////////                                          initialize Display 

const initializeDisplay = async () => {
    try {
        const data = await getData();
        console.log('printing initial data:');
        console.log(data);
        displayData(data);
    } catch (error) {
        console.error('Error fetching initial data:', error);
    }
}

document.getElementById('search-input').addEventListener('keyup', handleSortOrSearchChange);
document.getElementById('sort-dropdown').addEventListener('change', handleSortOrSearchChange);

// Call initializeDisplay to fetch and display initial data
initializeDisplay();

