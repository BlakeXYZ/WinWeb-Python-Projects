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

const handleSortChange = async () => {
    const data = await getData();
    const sortDropdown = document.getElementById('sort-dropdown');
    const selectedKey = sortDropdown.value;
    
    const sortedData = sortData(data, selectedKey);
    
    console.log('printing sorted data:');
    console.log(sortedData);

    displayData(sortedData);
};

// Initial display
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


// Add event listener to the dropdown for immediate sorting
const sortDropdown = document.getElementById('sort-dropdown');
sortDropdown.addEventListener('change', handleSortChange);


// Call initializeDisplay to fetch and display initial data
initializeDisplay();


// const my_apiEndpoint = "https://jsonplaceholder.typicode.com/users";
// const display_data = document.querySelector('#display-data');

// const getData = async () => {
//     // Fetch method to fetch Data
//     const res = await fetch(my_apiEndpoint);

//     // check if response is okay + handle errors
//     if (!res.ok){ throw new Error(`HTTP error! status: ${res.status}`) }

//     // Apply .json method to response
//     const data = await res.json();

//     return data
// }


// const displayUsers = async () => {

//     // called getData function and stored inside var: payload
//     const my_payload = await getData();

//     // set dataDisplay variable
//     let dataDisplay = my_payload.map((object) => {
//         // iterate through payload array object and extract data
//         console.log(object)

//         const { name, username } = object
        
//         return `
//         <div class="container">
//             <p>Name: ${name}</p>
//             <p>Username: ${username}</p>
//         </div>
//         `
//     });

//     display_data.innerHTML = dataDisplay;
// }

// displayUsers();