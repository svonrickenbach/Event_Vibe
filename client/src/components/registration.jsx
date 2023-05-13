import React, { useState } from 'react'
import { Link, useNavigate } from "react-router-dom";
import axios from 'axios';
import Cookies from 'js-cookie';
import 'bootstrap/dist/css/bootstrap.min.css';

const Registration = () => {
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
            password,
            confirmPassword
        })
            .then(res => {
                console.log(res);
                console.log(res.data);
                Cookies.set('token', res.data.token)
                navigate("/event");
            })
            .catch((err) => {
                console.log("error:", err);
                // setErrors(err.data.flash_message);
                setErrors(err.response.data.errors);
                console.log(err.response.data.errors);
            })
    }


    return (
        <div className="container d-flex align-items-center justify-content-center vh-100">
            <div className="row">
                <div className="col-sm-12">
                    <h2 className='mb-3'>Registration</h2>
                    <form onSubmit={onRegisterSubmitHandler}>
                        <div className="form-group mb-3">
                            <input type="text" onChange={(e) => setFirstName(e.target.value)} value={first_name} className="form-control" placeholder='Enter first name' />
                            {errors.first_name ? <p className='text-danger'>{errors.first_name}</p> : null}
                            {errors.first_name_min ? <p className='text-danger'>{errors.first_name_min}</p> : null}
                            {errors.first_name_reg ? <p className='text-danger'>{errors.first_name_reg}</p> : null}
                        </div>
                        <div className="form-group mb-3">
                            <input type="text" onChange={(e) => setLastName(e.target.value)} value={last_name} className="form-control" placeholder='Enter last name' />
                            {errors.last_name ? <p className='text-danger'>{errors.last_name}</p> : null}
                            {errors.last_name_min ? <p className='text-danger'>{errors.last_name_min}</p> : null}
                            {errors.last_name_reg ? <p className='text-danger'>{errors.last_name_reg}</p> : null}
                        </div>
                        <div className="form-group mb-3">
                            <input type="email" onChange={(e) => setEmail(e.target.value)} value={email} className="form-control" placeholder='Enter email' />
                            {errors.email ? <p className='text-danger'>{errors.email}</p> : null}
                            {errors.email_reg ? <p className='text-danger'>{errors.email_reg}</p> : null}
                            {errors.email_db ? <p className='text-danger'>{errors.email_db}</p> : null}
                        </div>
                        <div className="form-group mb-3">
                            <input type="password" onChange={(e) => setPassword(e.target.value)} value={password} className="form-control" placeholder='Enter password' />
                            {errors.password ? <p className='text-danger'>{errors.password}</p> : null}
                            {errors.password_len ? <p className='text-danger'>{errors.password_len}</p> : null}
                            {errors.password_reg ? <p className='text-danger'>{errors.password_reg}</p> : null}
                        </div>
                        <div className="form-group mb-3">
                            <input type="password" onChange={(e) => setConfirmPassword(e.target.value)} value={confirmPassword} className="form-control" placeholder='Confirm password' />
                            {errors.confirm_password ? <p className='text-danger'>{errors.confirm_password}</p> : null}
                            {errors.password_match ? <p className='text-danger'>{errors.password_match}</p> : null}
                        </div>
                        <button type="submit" className="btn btn-primary mb-3">Submit</button> <br />
                        <Link to="/">Login</Link>
                    </form>
                </div>
            </div>
        </div>
    );
};

export default Registration;