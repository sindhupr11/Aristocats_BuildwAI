"use client"
import CircularProgress from '@mui/material/CircularProgress';
import { getAuth, onAuthStateChanged } from 'firebase/auth';
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import LargeText from "../components/LargeText";
import SignOutButton from "../components/SignOutButton";
import SmallText from "../components/SmallText";





export default function Dashboard() {
  const router = useRouter();
  const [user, setUser] = useState(null);
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);


  const fetchBackendData = async (accessToken) => {
    setData("miskdfhsldk");
  };

  useEffect(() => {
    const auth = getAuth();

    const unsubscribe = onAuthStateChanged(auth, (currentUser) => {
      if (currentUser) {
        console.log(currentUser)
        setUser(currentUser);
        fetchBackendData(currentUser.accessToken);
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
