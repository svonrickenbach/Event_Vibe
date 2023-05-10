import React, { useState } from 'react'
import { useNavigate } from "react-router-dom";
import axios from 'axios';
import Cookies from 'js-cookie';
import 'bootstrap/dist/css/bootstrap.min.css';

const LoginRegistrationPage = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [first_name, setFirstName] = useState('');
    const [last_name, setLastName] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [errors, setErrors] = useState('');

    const navigate = useNavigate();


    const onRegisterSubmitHandler = (e) => {

        e.preventDefault();

        axios.post('http://127.0.0.1:5000/register', {
            first_name,
            last_name,
            email,
            password
        })
            .then(res => {
                console.log(res);
                console.log(res.data);
                Cookies.set('id', res.data.id)
                navigate("/event");
            })
            .catch((err) => {
                console.log(err);
                // setErrors(err.response.data.errors);
                // console.log(err.response.data.errors);
            })
    }

    const onLoginSubmitHandler = (e) => {

        e.preventDefault();

        axios.post('http://127.0.0.1:5000/login', {
            email,
            password
        })
            .then(res => {
                console.log(res);
                console.log(res.data);
                Cookies.set('id', res.data.id)
                navigate("/event");
            })
            .catch((err) => {
                console.log(err);
                // setErrors(err.response.data.errors);
                // console.log(err.response.data.errors);
            })
    }

    return (
        <div className="container">
            <div className="row mt-5">
                <div className="col-sm-6">
                    <h2>Registration</h2>
                    <form onSubmit={onRegisterSubmitHandler}>
                        <div className="form-group">
                            <label htmlFor="first_name">First Name</label>
                            <input type="text" onChange={(e) => setFirstName(e.target.value)} value={first_name} className="form-control" placeholder='Enter first name' />
                            {errors.first_name ? <p className='text-danger'>{errors.first_name.message}</p> : null}
                        </div>
                        <div className="form-group">
                            <label htmlFor="last_name">Last Name</label>
                            <input type="text" onChange={(e) => setLastName(e.target.value)} value={last_name} className="form-control" placeholder='Enter last name' />
                            {errors.last_name ? <p className='text-danger'>{errors.last_name.message}</p> : null}
                        </div>
                        <div className="form-group">
                            <label htmlFor="email">Email address</label>
                            <input type="text" onChange={(e) => setEmail(e.target.value)} value={email} className="form-control" placeholder='Enter email' />
                            {errors.email ? <p className='text-danger'>{errors.email.message}</p> : null}
                        </div>
                        <div className="form-group">
                            <label htmlFor="password">Password</label>
                            <input type="password" onChange={(e) => setPassword(e.target.value)} value={password} className="form-control" placeholder='Enter password' />
                            {errors.first_name ? <p className='text-danger'>{errors.password.message}</p> : null}
                        </div>
                        <div className="form-group">
                            <label htmlFor="confirmPassword">Confirm Password</label>
                            <input type="password" onChange={(e) => setConfirmPassword(e.target.value)} value={confirmPassword} className="form-control" placeholder='Enter password confirmation' />
                            {errors.confirmPassword ? <p className='text-danger'>{errors.password.message}</p> : null}
                        </div>
                        <button type="submit" className="btn btn-primary">Submit</button>
                    </form>
                </div>
                <div className="col-sm-6">
                    <h2>Login</h2>
                    <form onSubmit={onLoginSubmitHandler}>
                        <div className="form-group">
                            <label htmlFor="loginEmail">Email address</label>
                            <input type="text" onChange={(e) => setEmail(e.target.value)} value={email} className="form-control" placeholder='Enter email' />
                            {errors.email ? <p className='text-danger'>{errors.email.message}</p> : null}
                        </div>
                        <div className="form-group">
                            <label htmlFor="loginPassword">Password</label>
                            <input type="password" onChange={(e) => setPassword(e.target.value)} value={password} className="form-control" placeholder='Enter password' />
                            {errors.first_name ? <p className='text-danger'>{errors.password.message}</p> : null}
                        </div>
                        <button type="submit" className="btn btn-primary">Submit</button>
                    </form>
                </div>
            </div>
        </div>
    );
};

export default LoginRegistrationPage;