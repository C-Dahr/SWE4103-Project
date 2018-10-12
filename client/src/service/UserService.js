import ServiceLayer from '@/service/ServiceLayer';

export default {
  register(params) {
    return ServiceLayer().post('/register', params)
      .then((response) => {
        return response;
      })
      .catch((err) => {
        return err.response;
      });
  },
  login(params) {
    return ServiceLayer().post('/login', params)
      .then((response) => {
        console.log('Login Success: ', response);
        return response;
      })
      .catch((err) => {
        console.log('Login Err: ', err);
        return err.response;
      });
  },
};
