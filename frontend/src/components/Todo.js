import React from "react";
import {Table} from "antd";
const { Column } = Table;


const Todo = ({todo}) => {
    return (
        <Table dataSource={todo}>
            <Column title="TODO" dataIndex="todo" key="todo"/>
            <Column title="Text" dataIndex="text" key="text"/>
            <Column title="Created" dataIndex="create_date" key="create_date"/>
        </Table>
    )
}

export default Todo