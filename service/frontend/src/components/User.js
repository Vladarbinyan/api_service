import React from "react";
import {Table} from "antd";
const { Column } = Table;


const UserList = ({users}) => {
    return (
        <Table dataSource={users}>
            <Column title="Username" dataIndex="username" key="username"/>
            <Column title="First Name" dataIndex="firstname" key="firstname"/>
            <Column title="Last Name" dataIndex="lastname" key="lastname"/>
            <Column title="Email address" dataIndex="email" key="email"/>
        </Table>
    )
}

export default UserList
