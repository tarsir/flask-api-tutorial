import axios from 'axios';

const serverUrl = "http://localhost:5000";
let baseHeaders: HeadersInit = new Headers();
baseHeaders.set('Content-Type', 'application/json');

export async function get(endpoint: string, params: string[] = []) {
    let url = serverUrl + "/" + endpoint;

    const response = await axios.get(url);

    return await response.data;
}
