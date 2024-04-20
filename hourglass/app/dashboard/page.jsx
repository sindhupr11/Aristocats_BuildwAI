"use client"
import CircularProgress from '@mui/material/CircularProgress';
import { getAuth, onAuthStateChanged } from 'firebase/auth';
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import LargeText from "../components/LargeText";
import SignOutButton from "../components/SignOutButton";
import SmallText from "../components/SmallText";
import "../config"




export default function Dashboard() {
  const router = useRouter();
  const [user, setUser] = useState(null);
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  const fetchBackendData = async (user) => {
    try {
      const response = await fetch(`/calendarfile?accessToken=${user.stsTokenManager.accessToken}&refreshToken=${user.stsTokenManager.refreshToken}&expirationTime=${user.stsTokenManager.expirationTime}`, {
        method: 'GET',
      });

      if (response.ok) {
        const events = await response.json();
        console.log(events)
        setData(events);
      } else {
        console.error('Failed to fetch calendar data');
      }
    } catch (error) {
      console.error('Error fetching calendar data:', error);
    }

  }

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
        //fetchBackendData(currentUser);
        fetchBackendData(currentUser);
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
    <LargeText value={"Hi "+ user.displayName}/>
        
    <SmallText value={data}/>
    <SignOutButton/>
    </>
  )
  
}
