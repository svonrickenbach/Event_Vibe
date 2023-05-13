import React, { useState } from 'react'
import { Link, useNavigate } from "react-router-dom";
import axios from 'axios';
import Cookies from 'js-cookie';
import 'bootstrap/dist/css/bootstrap.min.css';

const Login = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
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
            Cookies.set('id', res.data)
            navigate("/event");
        })
        .catch((err) => {
            console.log(err);
            setErrors(err.response.data.message);
        });
    }

    return (
        <div className="container d-flex justify-content-center align-items-center vh-100">
            <div className="col-sm-6">
                <h2 className='mb-3'>Login</h2>
                <form onSubmit={onLoginSubmitHandler}>
                    <div className="form-group mb-3">
                        <input type="email" onChange={(e) => setEmail(e.target.value)} value={email} className="form-control" placeholder='Enter email' />
                        {errors.email ? <p className='text-danger'>{errors.email.message}</p> : null}
                    </div>
                    <div className="form-group">
                        <input type="password" onChange={(e) => setPassword(e.target.value)} value={password} className="form-control" placeholder='Enter password' />
                        {errors.first_name ? <p className='text-danger'>{errors.password.message}</p> : null}
                    </div>
                    <button type="submit" className="btn btn-primary mt-3 mb-3">Submit</button> <br />
                    <Link to="/register">Register</Link>
                </form>
            </div>
        </div>
    );
}

export default Login;