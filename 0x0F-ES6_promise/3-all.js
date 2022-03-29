import { uploadPhoto, createUser } from './utils';

export default async function handleProfileSignup() {
  try {
    const userupload = await createUser();
    const photo = await uploadPhoto();
    console.log(`${photo.body} ${userupload.firstName} ${userupload.lastName}`);
  } catch (err) {
    console.log('Signup system offline');
  }
}
