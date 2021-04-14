import { useState } from 'react'

export default function LoginForm({ onSubmit }) {

    const initialValues = {
        username: '',
        password: '',
    }

    const [values, setValues] = useState(initialValues);

    function submitHandler(event) {
        event.preventDefault();
        onSubmit(values);
        setValues(initialValues)
    }

    function inputChangeHandler(event) {

        let { name, value } = event.target;

        setValues({ ...values, [name]: value });
    }

    return (

        <form onSubmit={submitHandler}>
            <div>
                <label htmlFor="username">User Name</label>
                <input type="text" name="username" id="username" value={values.username} onChange={inputChangeHandler} placeholder="User Name" />
            </div>

            <div>
                <label htmlFor="password">Password</label>
                <input type="password" name="password" id="password" value={values.password} onChange={inputChangeHandler} placeholder="password" />
            </div>

            <button type="submit">Sign In</button>

        </form>
    );
}
