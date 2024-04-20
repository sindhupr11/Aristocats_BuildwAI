

const TextComponent = ({ children }) => {
    return (
      <h1 className="scroll-m-20 text-2xl text-center font-extrabold tracking-tight lg:text-2xl m-5" style={{maxWidth:"40%", minWidth:"200px"}}>
        
        {children}
      </h1>
    );
  };
  
  export default TextComponent;
  