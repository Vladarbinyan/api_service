import React from "react";
import { Table } from 'antd';

const UserItem = ({user}) => {
    return (
        <tr>
            <td>
                {user.username}
            </td>
            <td>
                {user.firstname}
            </td>
            <td>
                {user.lastname}
            </td>
            <td>
                {user.email}
            </td>
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <table>
            <th>
                Username
            </th>
            <th>
                First name
            </th>
            <th>
                Last name
            </th>
            <th>
                Email address
            </th>
            {users.map((users) => <UserItem user={users} /> )}
        </table>
    )
}

export default UserList
