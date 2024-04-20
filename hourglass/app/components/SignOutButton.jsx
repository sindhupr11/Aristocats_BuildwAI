"use client"
import { Button } from "@/components/ui/button";
import { useRouter } from "next/navigation";
import { auth } from '../config';

const SignOutButton = () => {
  const router = useRouter();

  const handleSignOut = () => {
    auth.signOut().then(() => {
      router.push('/');
    });
  };

  return (
    <Button 
      variant="outline" 
      onClick={handleSignOut} 
      style={{ backgroundColor: "white", color: "black" }}
    >
      Sign Out
    </Button>
  );
};

export default SignOutButton;
