import React from "react";
import {Table} from "antd";

const {Column} = Table;


const Project = ({projects}) => {
    return (
        <Table dataSource={projects}>
            <Column title="Project" dataIndex="title" key="title"/>
        </Table>
    )
}

export default Project