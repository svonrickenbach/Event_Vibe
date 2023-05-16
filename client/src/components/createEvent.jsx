import React, { useState } from 'react'
import { Link, useNavigate } from "react-router-dom";
import axios from 'axios';
import Cookies from 'js-cookie';
import 'bootstrap/dist/css/bootstrap.min.css';

const CreateEvent = () => {
    const [title, setTitle] = useState('');
    const [date, setDate] = useState('');
    // const [time, setTime] = useState('');
    const [location, setLocation] = useState('');
    const [description, setDescription] = useState('');
    const [image, setImage] = useState('');
    const [user_id, setUserId] = useState('');
    const [errors, setErrors] = useState('');
    const token = Cookies.get('token');
    const navigate = useNavigate();

    if (!token) {
        navigate('/');
    }

    const onSubmit = (e) => {

        e.preventDefault();
        console.log(token)
        axios.post('http://127.0.0.1:5000/event', {
            title,
            date,
            // time,
            location,
            description,
            image,
            user_id
        }, {
            headers: { 'Authorization': `Bearer ${token}` }
        })
            .then(res => {
                console.log(res);
                console.log(res.data);
                navigate("/dashboard");
            })
            .catch((err) => {
                console.log(err);
                setErrors(err.response.data.errors);
                console.log(err.response.data.errors);
            })
    }


    return (
        <div className="container d-flex align-items-center justify-content-center vh-100">
            <div className="row">
                <div className="col-sm-12">
                    <h2 className='mb-3'>Add an Event!</h2>
                    <form onSubmit={onSubmit}>
                        <div className="form-group mb-3">
                            <input type="text" onChange={(e) => setTitle(e.target.value)} value={title} className="form-control" placeholder='Enter a title' />
                            {errors.title ? <p className='text-danger'>{errors.title}</p> : null}
                            {errors.title_min ? <p className='text-danger'>{errors.title_min}</p> : null}
                        </div>
                        <div className="form-group mb-3">
                            <input type="date" onChange={(e) => setDate(e.target.value)} value={date} className="form-control" placeholder='Enter last name' />
                            {errors.date ? <p className='text-danger'>{errors.date}</p> : null}
                            {errors.date_future ? <p className='text-danger'>{errors.date_future}</p> : null}
                        </div>
                        {/* <div className="form-group mb-3">
                            <input type="time" onChange={(e) => setTime(e.target.value)} value={time} className="form-control" placeholder='Enter email' />
                            {errors.time ? <p className='text-danger'>{errors.time}</p> : null}
                        </div> */}
                        <div className="form-group mb-3">
                            <input type="text" onChange={(e) => setLocation(e.target.value)} value={location} className="form-control" placeholder='Enter a location' />
                            {errors.location ? <p className='text-danger'>{errors.location}</p> : null}
                            {errors.location_min ? <p className='text-danger'>{errors.location_min}</p> : null}
                        </div>
                        <div className="form-group mb-3">
                            <input type="text-area" onChange={(e) => setDescription(e.target.value)} value={description} className="form-control" placeholder='Enter a description' />
                            {errors.description ? <p className='text-danger'>{errors.description}</p> : null}
                        </div>
                        <input type="hidden" onChange={(e) => setUserId(null)} />
                        <button type="submit" className="btn btn-primary mb-3">Submit</button> <br />
                        <Link to="/dashboard">Dashboard</Link>
                    </form>
                </div>
            </div>
        </div>
    );
};

export default CreateEvent;