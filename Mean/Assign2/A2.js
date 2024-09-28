function showBookTopics(bookId) {
    const topicsDiv = document.getElementById(`book-topics-${bookId}`);
    if (topicsDiv.style.display === 'none' || topicsDiv.style.display === '') {
        topicsDiv.style.display = 'block';
    } else {
        topicsDiv.style.display = 'none';
    }
}

function submitOrder() {
    // Clear previous error messages
    document.querySelectorAll('.error-message').forEach(el => el.textContent = '');

    // Get form values
    const name = document.getElementById('customer-name').value.trim();
    const address = document.getElementById('customer-address').value.trim();
    const paymentDetails = document.getElementById('payment-details').value.trim();
    const copies = document.getElementById('number-of-copies').value.trim();

    let isValid = true;

    // Validate that no field is left blank and display error messages accordingly
    if (!name) {
        const nameError = document.getElementById('name-error');
        nameError.textContent = 'Name is required';
        nameError.style.color = 'red';
        nameError.style.fontWeight = 'bold';
        isValid = false;
    }

    if (!address) {
        const addressError = document.getElementById('address-error');
        addressError.textContent = 'Address is required';
        addressError.style.color = 'red';
        addressError.style.fontWeight = 'bold';
        isValid = false;
    }

    if (!paymentDetails) {
        const paymentError = document.getElementById('payment-error');
        paymentError.textContent = 'Payment details are required';
        paymentError.style.color = 'red';
        paymentError.style.fontWeight = 'bold';
        isValid = false;
    }

    if (!copies) {
        const copiesError = document.getElementById('copies-error');
        copiesError.textContent = 'Number of copies is required';
        copiesError.style.color = 'red';
        copiesError.style.fontWeight = 'bold';
        isValid = false;
    } else if (isNaN(copies) || copies <= 0) {
        const copiesError = document.getElementById('copies-error');
        copiesError.textContent = 'Number of copies must be a positive number';
        copiesError.style.color = 'red';
        copiesError.style.fontWeight = 'bold';
        isValid = false;
    }

    // Display order confirmation if form is valid
    if (isValid) {
        const orderStatus = document.getElementById('order-status');
        orderStatus.innerText = 'Order Confirmed';
        orderStatus.style.color = 'green';
        document.getElementById('order-response').style.display = 'block';
    }
}
