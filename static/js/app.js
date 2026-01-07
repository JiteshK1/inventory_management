const API_URL = "/api/items/";

document.addEventListener("DOMContentLoaded", fetchItems);

function fetchItems() {
    fetch(API_URL)
        .then(res => res.json())
        .then(data => {
            const table = document.getElementById("items-table");
            table.innerHTML = "";

            data.results.forEach(item => {
                table.innerHTML += `
                    <tr>
                        <td>${item.id}</td>
                        <td>${item.name}</td>
                        <td>${item.quantity}</td>
                        <td>${item.price}</td>
                        <td>
                            <button onclick="editItem(${item.id})">Edit</button>
                            <button onclick="deleteItem(${item.id})">Delete</button>
                        </td>
                    </tr>
                `;
            });
        });
}

function saveItem() {
    const id = document.getElementById("item-id").value;

    const payload = {
        name: document.getElementById("name").value,
        quantity: document.getElementById("quantity").value,
        price: document.getElementById("price").value,
        description: document.getElementById("description").value,
    };

    const method = id ? "PUT" : "POST";
    const url = id ? `${API_URL}${id}/` : API_URL;

    fetch(url, {
        method: method,
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
    })
    .then(() => {
        clearForm();
        fetchItems();
    });
}

function editItem(id) {
    fetch(`${API_URL}${id}/`)
        .then(res => res.json())
        .then(item => {
            document.getElementById("item-id").value = item.id;
            document.getElementById("name").value = item.name;
            document.getElementById("quantity").value = item.quantity;
            document.getElementById("price").value = item.price;
            document.getElementById("description").value = item.description;
        });
}

function deleteItem(id) {
    if (!confirm("Delete this item?")) return;

    fetch(`${API_URL}${id}/`, {
        method: "DELETE"
    })
    .then(fetchItems);
}

function clearForm() {
    document.getElementById("item-id").value = "";
    document.getElementById("name").value = "";
    document.getElementById("quantity").value = "";
    document.getElementById("price").value = "";
    document.getElementById("description").value = "";
}
