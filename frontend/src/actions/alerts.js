import { message } from 'antd';

// Alerts

export const sucessAlert = (text) => {
  message.success(text);
};
export const errorAlert = (text) => {
  message.error(text);
};
