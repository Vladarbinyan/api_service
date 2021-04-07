import React from "react";
import {Table} from "antd";
const { Column } = Table;


const User = ({users}) => {
    return (
        <Table dataSource={users}>
            <Column title="Username" dataIndex="username" key="username"/>
            <Column title="First Name" dataIndex="first_name" key="first_name"/>
            <Column title="Last Name" dataIndex="last_name" key="last_name"/>
            <Column title="Email address" dataIndex="email" key="email"/>
        </Table>
    )
}

export default User
