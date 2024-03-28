import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
    return (
        <nav>
            <ul>
                <li><Link to="/">Home</Link></li>
                <li><Link to="/user-account">User Account</Link></li>
            </ul>
        </nav>
    );
}

export default Navbar;