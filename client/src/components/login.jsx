import React, { useState } from 'react'
import { Link, useNavigate } from "react-router-dom";
import axios from 'axios';
import Cookies from 'js-cookie';
import 'bootstrap/dist/css/bootstrap.min.css';

const Login = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [errors, setErrors] = useState('');

    const navigate = useNavigate();

    const onLoginSubmitHandler = (e) => {
        e.preventDefault();

        axios.post('http://127.0.0.1:5000/login', {
            email,
            password
        })
        .then(res => {
            console.log(res);
            console.log(res.data);
            Cookies.set('token', res.data.token);
            navigate("/dashboard");
        })
        .catch((err) => {
            console.log(err.response.data);
            setErrors(err.response.data);
        });
    }

    return (
        <div className="container d-flex justify-content-center align-items-center vh-100">
            <div className="col-sm-6">
                <h2 className='mb-3'>Login</h2>
                <form onSubmit={onLoginSubmitHandler}>
                    <div className="form-group mb-3">
                        <input type="email" onChange={(e) => setEmail(e.target.value)} value={email} className="form-control" placeholder='Enter email' />
                    </div>
                    <div className="form-group">
                        <input type="password" onChange={(e) => setPassword(e.target.value)} value={password} className="form-control" placeholder='Enter password' />
                        {errors.error ? <p className='text-danger'>{errors.error}</p> : null}
                    </div>
                    <button type="submit" className="btn btn-primary mt-3 mb-3">Submit</button> <br />
                    <Link to="/register">Register</Link>
                </form>
            </div>
        </div>
    );
}

export default Login;