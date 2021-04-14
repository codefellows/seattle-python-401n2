import { useState } from 'react'
import { getToken } from '../services/data-fetcher'


export default function Home() {

    const [token, setToken] = useState();

    const [username, setUsername] = useState('');

    async function loginHandler(values) {

        const fetchedToken = await getToken(values);

        setToken(fetchedToken);

        setUsername(values.username);
    }

    function logoutHandler() {
        setToken(null);
    }

    if (!token) return <h2>Show Login Form</h2>

    return <h2>Show the Cookie Stand Admin</h2>
}


