import React from "react";


import { Card, Avatar, Space } from 'antd';
import {EnvironmentFilled, CoffeeOutlined,UserOutlined,FileAddFilled } from '@ant-design/icons';

const { Meta } = Card;

export default function Home() {
  return(
  <Space size='large'>
    <Card hoverable
    style={{ backgroundColor:'#f9fcfb',borderRadius:'3px' }}
    actions={[
      <UserOutlined key="Speakers" />,
      <FileAddFilled key="Add Speaker" />,
    ]}
  >
    <Meta
      avatar={<Avatar style={{ backgroundColor: '#0f4c75' }} size={64} icon={<UserOutlined/>}/>}
      title="Speakers"
      description="This will be speaker description"
    />
  </Card>
    <Card hoverable
    style={{ backgroundColor:'#f9fcfb',borderRadius:'3px' }}
    actions={[
      <UserOutlined key="Speakers" />,
      <FileAddFilled key="Add Speaker" />,
    ]}
    >
    <Meta
      avatar={<Avatar style={{ backgroundColor: '#87d068' }} size={64} icon={<EnvironmentFilled/>}/>}
      title="Events"
      description="This will be event description"
    />
  </Card>
  <Card hoverable
    style={{ backgroundColor:'#f9fcfb',borderRadius:'3px' }}
    actions={[
      <UserOutlined key="Speakers" />,
      <FileAddFilled key="Add Speaker" />,
    ]}
  >
    <Meta
      avatar={<Avatar style={{ backgroundColor: '#b52b65' }} size={64} icon={<CoffeeOutlined/>}/>}
      title="Conference"
      description="This will be Conference description"
    />
  </Card>

  </Space>);
}



