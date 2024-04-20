"use client"
import 'firebase/auth';
import LargeText from "../components/LargeText";
import "../config"
import SignInButton from "../components/SignInButton";

const GoogleSignIn = () => {

  return (
    <>
    <LargeText value={"Please Sign In"}/>
    <SignInButton />
    </>
  );
};

export default GoogleSignIn;
