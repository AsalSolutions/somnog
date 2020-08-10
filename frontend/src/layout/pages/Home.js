import React from "react";
import {connect} from 'react-redux';



import { Card, Avatar, Space } from 'antd';
import {EnvironmentFilled, CoffeeOutlined,UserOutlined,FileAddFilled } from '@ant-design/icons';

const { Meta } = Card;

function Home({app}) {
  // Translate 
  const speakers = app.language === "EN" ? "Speakers" : "Khudbo-jeediye"
  const speakerCardDescription = app.language === "EN" ? "This will be speaker description" : "Halkan ayaad ka ogaan kartaa dhamaan macluumaadka ku saabsan khudbo-jeediyaasha";
  const events = app.language === "EN" ? "Events" : "Dhacdooyinka"
  const eventsCardDescription = app.language === "EN" ? "This will be events description" : "Halkan ayaad ka ogaan kartaa dhamaan macluumaadka ku saabsan Dhacdooyinka";
  const conference = app.language === "EN" ? "Conference" : "Shirarka"
  const conferenceCardDescription = app.language === "EN" ? "This will be conference description" : "Halkan ayaad ka ogaan kartaa dhamaan macluumaadka ku saabsan shirka";
  
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
      // title="Speakers"
      title={speakers}
      
      description={speakerCardDescription}
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
      title={events}
      description={eventsCardDescription}
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
      title={conference}
      description={conferenceCardDescription}
    />
  </Card>

  </Space>);
}

const mapStateToProps = (state) => {
  return {app:state.language}
}

export default connect(mapStateToProps)(Home);



