
exports.handler = async (event, context) => {
  
  try{
    console.log(event);
    return 'Sucess';
  }catch(error){
    console.error(error);
    throw error
  }
};