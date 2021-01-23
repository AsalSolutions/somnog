import jwt_decode from 'jwt-decode';
export default function tokenDecoder() {
  // Get token from session Storage
  const token = sessionStorage.getItem('token');
  if (!token) {
    return false;
  }
  const { identity } = jwt_decode(sessionStorage.getItem('token'));
  const { id, role } = identity.payload;
  return { userId: id, userRole: role };
}
