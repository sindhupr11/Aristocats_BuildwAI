"use client"
import 'firebase/auth';
import LargeText from "../components/LargeText";
import "../config"
import SignInButton from "../components/SignInButton";

const GoogleSignIn = () => {

  return (
    <div className='w-full'>
    <LargeText value={"Welcome to Hourglass"}/>
    <div style={{margin:"auto"}}><SignInButton /></div>
    </div>    
  );
};

export default GoogleSignIn;
