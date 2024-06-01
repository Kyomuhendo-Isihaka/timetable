function showNotification(message) {
    const notification = document.getElementById('notification');
    notification.textContent = message;
    notification.style.display = 'block';

    // Hide the notification after 3 seconds
    setTimeout(() => {
        notification.style.display = 'none';
    }, 5000);
}

function performAction() {
    // Simulate an action
    console.log('Action performed!');

    // Display notification
    showNotification('Action was successful!');
}
