"use client"
import CircularProgress from '@mui/material/CircularProgress';
import { getAuth, onAuthStateChanged } from 'firebase/auth';
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import LargeText from "../components/LargeText";
import SignOutButton from "../components/SignOutButton";
import SmallText from "../components/SmallText";
import "../config"
import Feed from "../components/Feed"



export default function Dashboard() {
  const router = useRouter();
  const [user, setUser] = useState(null);
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

/***
  const fetchBackendData = async (user) => {
    const oauth2Client = new google.auth.OAuth2(
      process.env.AUTH_GOOGLE_ID,
      process.env.AUTH_GOOGLE_SECRET,
      process.env.NEXTAUTH_URL + '/api/callback'
    );
  
    oauth2Client.setCredentials({
      access_token: session.accessToken,
      refresh_token: session.refreshToken,
      scope: 'https://www.googleapis.com/auth/calendar.readonly',
      token_type: 'Bearer',
      expiry_date: session.expires * 1000,
    });
  

      const events = await calendar.events.list({
        auth: oauth2Client,
        calendarId: 'primary',
        timeMin: new Date().toISOString(),
        maxResults: 10,
        singleEvents: true,
        orderBy: 'startTime',
      });

  }
 */
  useEffect(() => {
    const auth = getAuth();

    const unsubscribe = onAuthStateChanged(auth, (currentUser) => {
      if (currentUser) {
        console.log(currentUser)
        setUser(currentUser);
        let accesstoken = currentUser.stsTokenManager.accessToken
        let expirationtime = currentUser.stsTokenManager.expirationTime
        let refreshtoken = currentUser.stsTokenManager.refreshToken
        console.log(accesstoken ,expirationtime, refreshtoken)
        ////fetchBackendData(currentUser);
        setLoading(false)
      } else {
        router.push('/signin'); 
      }
    });

    return () => unsubscribe();
  }, []);

  if (!user || loading) {
    return (<>
    <CircularProgress color="secondary" size={"3em"} />
    </>
    ); 
  }

    return (
      <>
    <nav className='flex flex-row justify-between px-8 py-4 bg-slate-800'>
    
    <div className='flex flex-row mx-4'>
    <img src={user.photoURL} alt="Profile" className='w-12 h-12 rounded-full mr-2' /> 
      <h2 className='text-xl text-white my-auto '>
      Hey, {user.displayName}
    </h2>
    </div>   
    <SignOutButton/>
    </nav>
    <Feed/>
    </>
  )
  
}
