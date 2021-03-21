import React from "react";
import {Table} from "antd";

const {Column} = Table;


const Project = ({projects}) => {
    return (
        <Table dataSource={projects} rowKey={el => el.project_id}>
            <Column title="Project" dataIndex="title" key="title"/>
            <Column
                title="id"
                key="id"
                render={(text, record) => (<div>{}</div>)}
            />
        </Table>
    )
}

export default Project