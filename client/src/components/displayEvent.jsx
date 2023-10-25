import React, { useState, useEffect } from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import { Link, useNavigate, useParams } from 'react-router-dom';
import axios from 'axios';
import Cookies from 'js-cookie';

const EventDisplay = (props) => {
    const [event, setEvent] = useState([]);
    const navigate = useNavigate();
    const {id} = useParams(); 
    const [users, setUsers] = useState([]);
    // console.table(events)
    const token = Cookies.get('token');
    const [selectedUser, setSelectedUser] = useState(''); // Track the selected user
    const [allUsers, setAllUsers] = useState([]);

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

    useEffect(() => {
        if (!token) {
            navigate('/');
        }
        console.log(token);
        axios.get(`http://127.0.0.1:5000/`, {
            headers: { 'Authorization': `Bearer ${token}` }
        })
            .then((res) => {
                // console.log(res);
                setAllUsers(res.data);
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

    const setInvite = (eventId, selectedUser) => {
        // console.log("event id:" + events.id)
        console.log("selected user id" + selectedUser.id)
        const user_invite_id = selectedUser.id
        const event_id = eventId
        axios.post('http://127.0.0.1:5000/invite', {
            user_invite_id, event_id
        })
        .then((res) => {
            // console.log(res.data);
            setUsers(res.data);
        })
        .catch((err) => {
            // console.log(err);
        }, [])
    }

    return (
        <div>
            <h1>Event Details</h1>
            <Link to={"/dashboard"}className="mb-3">Dashboard</Link>
            <br></br>
            <Link to="/event/create" className="mb-3">Add Event</Link>
            <p>Title: {event.title}</p>
            <p>Date: {formatDate(event.date)}</p>
            {/* <p>Time: {event.time}</p> */}
            <p>Location: {event.location}</p>
            <p>Description: {event.description}</p>
            <Link to={"/event/update/" + event.id}className="mb-3">Edit</Link>
            <br/>
            <select value={selectedUser} onChange={(e) => setSelectedUser(e.target.value)}>
                <option value="">Select a user to invite</option>
                {allUsers.map((user) => (
                    <option key={user.id} value={user.id}>
                        {user.first_name} {/* Use the relevant user property */}
                    </option>
                ))}
            </select>
            <br/>
            <button onClick={(e) => { setInvite(event.id, selectedUser) }}>
                Invite
            </button>
            <br></br>
            <button onClick={(e)=>{deleteEvent(event.id)}}>
                Delete
            </button>
        </div>
    );
};

export default EventDisplay;