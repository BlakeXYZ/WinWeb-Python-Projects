const my_apiEndpoint = "./db/scanned_card_data.json";
const display_data = document.querySelector('#display-data');

const getData = async () => {
    // Fetch method to fetch Data
    const res = await fetch(my_apiEndpoint);

    // check if response is okay + handle errors
    if (!res.ok){ throw new Error(`HTTP error! status: ${res.status}`) }

    // Apply .json method to response
    const data = await res.json();

    return data
}


const displayUsers = async () => {

    // called getData function and stored inside var: payload
    const my_payload = await getData();
    console.log(my_payload)

    // set dataDisplay variable
    let dataDisplay = my_payload.map((object) => {
        // iterate through payload array object and extract data
        console.log(object)

        const { name, usdPrice, rarity, urlLink, urlThumbnailImage, confidenceValue } = object;

        return `
            <div class="container">
                <img src="${urlThumbnailImage}" alt="${name} Thumbnail">

                <div class="text-container">
                    <p><strong>Name:</strong> ${name}</p>
                    <p><strong>USD Price:</strong> $${usdPrice}</p>
                    <p><strong>Rarity:</strong> ${rarity}</p>
                    <p><strong>Confidence Value:</strong> ${confidenceValue}</p>
                    <p><a href="${urlLink}" target="_blank"><strong>Scryfall URL Link</strong></a></p>
                </div>
            </div>
        `
    }).join(''); // Use join('') to concatenate the array elements without commas

    display_data.innerHTML = dataDisplay;
}

displayUsers();

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