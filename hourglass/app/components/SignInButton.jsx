"use client"
import { Button } from "@/components/ui/button";
import { GoogleAuthProvider, getAuth, signInWithPopup } from "firebase/auth";
import { useRouter } from "next/navigation";
import "../config"
const provider = new GoogleAuthProvider();

const SignInButton = () => {
  const router = useRouter();

  const handleSignIn = () => {
    const auth = getAuth();
    signInWithPopup(auth, provider)
      .then((result) => {
        const credential = GoogleAuthProvider.credentialFromResult(result);
        const token = credential.accessToken;
        const user = result.user;
        router.push('/dashboard');
      })
      .catch((error) => {
        const errorCode = error.code;
        const errorMessage = error.message;
        const email = error.customData.email;
        const credential = GoogleAuthProvider.credentialFromError(error);
      });
  };

  return (
    <Button 
      variant="outline" 
      onClick={handleSignIn} 
      style={{ backgroundColor: "white", color: "black" }}
    >
      Sign In
    </Button>
  );
};

export default SignInButton;
