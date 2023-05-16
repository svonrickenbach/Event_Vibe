import React, { useState, useEffect } from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import { Link, useNavigate, useParams } from 'react-router-dom';
import axios from 'axios';
import Cookies from 'js-cookie';

const EventDisplay = (props) => {
    const [event, setEvent] = useState([]);
    const navigate = useNavigate();
    const {id} = useParams(); 
    // console.table(events)
    const token = Cookies.get('token');

    useEffect(() => {
        if (!token) {
            navigate('/');
        }
        console.log(token);
        axios.get(`http://127.0.0.1:5000/event/${id}`, {
            headers: { 'Authorization': `Bearer ${token}` }
        })
            .then((res) => {
                // console.log(res);
                setEvent(res.data);
            })
            .catch((err) => {
                // console.log(err);
            })
    }, [])

    const deleteEvent = (id) => {
        axios.delete(`http://127.0.0.1:5000/event/${id}`, {
            headers: { 'Authorization': `Bearer ${token}` }
        })
            .then(res => {
                console.log(res);
                navigate("/dashboard");
            })
            .catch(err => console.log(err))
        }

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
        <div>
            <h1>Event Details</h1>
            <p>Title: {event.title}</p>
            <p>Date: {formatDate(event.date)}</p>
            <p>Location: {event.location}</p>
            <p>Description: {event.description}</p>
            <Link to={"/event/update/" + event.id}className="mb-3">Edit</Link>
            <br/>
            <button onClick={(e)=>{deleteEvent(event.id)}}>
                Delete
            </button>
        </div>
    );
};

export default EventDisplay;