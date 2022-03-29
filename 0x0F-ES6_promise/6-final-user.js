import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, filename) {
  const sign = await signUpUser(firstName, lastName);
  const photo = await uploadPhoto(filename);

  return [
    { value: sign, status: 'fulfilled' },
    { value: photo.catch((err) => err), status: 'rejected' },
  ];
}
