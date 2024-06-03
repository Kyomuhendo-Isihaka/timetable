// Function to get the current date
function getCurrentDate() {
    const date = new Date(); // Create a new Date object with the current date and time

    // Format the date
    const year = date.getFullYear();
    const month = ('0' + (date.getMonth() + 1)).slice(-2); // Months are zero-based, so add 1
    const day = ('0' + date.getDate()).slice(-2);

    // Combine into a string
    const formattedDate = `${day}/${month}/${year}`;

    // Display the date
    document.getElementById('current-date').textContent = formattedDate;
}

// Call the function to display the current date when the page loads
window.onload = getCurrentDate;
