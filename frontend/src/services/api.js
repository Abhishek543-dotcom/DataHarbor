// src/services/api.js
const BASE_URL = 'http://localhost:5000/api';

export const fetchData = async (endpoint) => {
    const response = await fetch(`${BASE_URL}/${endpoint}`);
    return response.json();
};

export const postData = async (endpoint, data) => {
    const response = await fetch(`${BASE_URL}/${endpoint}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });
    return response.json();
};
