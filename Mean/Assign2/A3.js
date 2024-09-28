document.getElementById('contact-form').addEventListener('submit', function(e) {
    e.preventDefault();

    const name = document.getElementById('name').value.trim();
    const address = document.getElementById('address').value.trim();
    const phone = document.getElementById('phone').value.trim();

    // Validation for name (only alphabets)
    const namePattern = /^[A-Za-z\s]+$/;
    if (!namePattern.test(name)) {
        alert('Name should contain only alphabets');
        return;
    }

    // Validation for phone number (numeric and 10 digits)
    const phonePattern = /^\d{10}$/;
    if (!phonePattern.test(phone)) {
        alert('Phone number should be numeric and exactly 10 digits long');
        return;
    }

    if (address === '') {
        alert('Please fill in the address');
        return;
    }

    const contact = {
        id: Date.now(),
        name: name,
        address: address,
        phone: phone
    };

    let contacts = JSON.parse(localStorage.getItem('contacts')) || [];
    contacts.push(contact);
    localStorage.setItem('contacts', JSON.stringify(contacts));

    addContactToList(contact);

    document.getElementById('contact-form').reset();
});

function addContactToList(contact) {
    const contactList = document.getElementById('contact-list');
    const card = document.createElement('div');
    card.classList.add('card');
    card.setAttribute('data-id', contact.id);

    card.innerHTML = `
        <h3>${contact.name}</h3>
        <p>${contact.address}</p>
        <p>${contact.phone}</p>
        <button class="delete-btn">Delete</button>
    `;

    contactList.appendChild(card);
}

document.getElementById('contact-list').addEventListener('click', function(e) {
    if (e.target.classList.contains('delete-btn')) {
        const id = e.target.parentElement.getAttribute('data-id');
        e.target.parentElement.remove();

        let contacts = JSON.parse(localStorage.getItem('contacts'));
        contacts = contacts.filter(contact => contact.id !== parseInt(id));
        localStorage.setItem('contacts', JSON.stringify(contacts));
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const contacts = JSON.parse(localStorage.getItem('contacts')) || [];
    contacts.forEach(contact => addContactToList(contact));
});
