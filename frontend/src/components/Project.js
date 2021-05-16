import React from "react";
import {Table, Space} from "antd";

const {Column} = Table;


const Project = ({projects, deleteProject}) => {
    return (
        <Table dataSource={projects}>
            <Column
                title="Action"
                key="action"
                render={(text, record) => (
                    <Space size="middle">
                        <a>Modify</a>
                        <a onClick={()=>deleteProject(record.uuid)} >Delete</a>
                    </Space>
                )}
            />
            <Column title="Project" dataIndex="title" key="title"/>
        </Table>
    )
}

export default Project