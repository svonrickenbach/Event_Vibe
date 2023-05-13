import React, { useState, useEffect } from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';
import Cookies from 'js-cookie';

const EventList = (props) => {
    const [events, setEvents] = useState([]);
    const [users, setUsers] = useState([]);
    const navigate = useNavigate();
    // console.table(events)
    const token = Cookies.get('token');

    useEffect(() => {
        if (!token) {
            navigate('/');
        }
        console.log(token);
        axios.get(`http://127.0.0.1:5000/event`, {
            headers: { 'Authorization': `Bearer ${token}` }
        })
            .then((res) => {
                // console.log(res);
                setEvents(res.data);
            })
            .catch((err) => {
                // console.log(err);
            })
    }, [])

    useEffect(() => {
        axios.get(`http://127.0.0.1:5000/oneuser`, {
            headers: {
                'Authorization': `Bearer ${token}`,
            }
        })
            .then((res) => {
                // console.log(res.data);
                setUsers(res.data);
            })
            .catch((err) => {
                // console.log(err);
            })
    }, [])

    const formatDate = (dateString) => {
        const options = { weekday: 'long', month: 'long', day: 'numeric' };
        const date = new Date(dateString);
        const formattedDate = date.toLocaleDateString('en-US', options);
        return formattedDate;
    }

    const handleLogout = (e) => {
        e.preventDefault();

        Cookies.remove('token')
        navigate('/');
    }


    return (
        <div className="container mt-3">
            <div className="row">
                <div className="col-2 bg-light left">
                    <div className="text-center">
                        <h4>{users.first_name} {users.last_name}</h4>
                    </div>
                    <div className="list-group">
                        <Link to="#" className="mb-3">Add Event</Link>
                        <Link to="#" className="mb-3">Event Map</Link>
                        <Link to="#" className="mb-3">Friends</Link>
                        <Link to="#" className="mb-3">Settings</Link>
                    </div>
                    <div className="text-center mt-3">
                        <button type="button" className="btn btn-secondary" onClick={handleLogout}>Logout</button>
                    </div>
                </div>
                <div className="col-10 right">
                    <div className="row">
                        <div className="col mt-5 mb-3">
                            <div className="text-center">
                                <h1>Event List</h1>
                            </div>
                        </div>
                        <div className="col-auto">
                            <div className="input-group mb-3">
                                <input type="text" className="form-control" placeholder="Search" aria-label="Search" aria-describedby="button-addon2" />
                                <button className="btn btn-outline-secondary" type="button" id="button-addon2">Search</button>
                            </div>
                        </div>
                    </div>
                    <div className="row">
                        <div className="col">
                            <ul className="list-group">
                                {events.map((event) => (
                                    <li key={event.id} className="list-group-item">
                                        <div className="row align-items-center">
                                            <div className="col-auto">
                                                <img src={event.imageUrl} alt={event.title} width="100" height="100" />
                                            </div>
                                            <div className="col">
                                                <div>
                                                    {formatDate(event.date)} <br />
                                                    {event.title} <br />
                                                    {event.location}
                                                </div>
                                            </div>
                                        </div>
                                    </li>
                                ))}
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default EventList;