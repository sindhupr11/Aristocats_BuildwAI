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


  const fetchBackendData = async (accessToken) => {
    setData("miskdfhsldk");
  };

  useEffect(() => {
    const auth = getAuth();

    const unsubscribe = onAuthStateChanged(auth, (currentUser) => {
      if (currentUser) {
        console.log(currentUser)
        setUser(currentUser);
        //fetchBackendData(currentUser.accessToken);
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
