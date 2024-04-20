import { cn } from "@/lib/utils";
import { ThemeProvider } from "next-themes";
import { Inter as FontSans } from "next/font/google";
import 'react-awesome-button/dist/styles.css';
import './globals.css';

const fontSans = FontSans({
  subsets: ["latin"],
  variable: "--font-sans",
})
import "./config"

import 'firebase/auth';


export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={cn(
          "min-h-screen bg-background font-sans antialiased",
          fontSans.variable
        )}>
          <ThemeProvider
            attribute="class"
            defaultTheme="dark"
            enableSystem
            disableTransitionOnChange
          >
            <div style={{justifyContent:"center", display:"flex", alignItems:"center", alignContent:"center", height:"100vh", flexDirection:"column"}}>
        {children}
        </div>
        </ThemeProvider>
        </body>
    </html>
  );
}
