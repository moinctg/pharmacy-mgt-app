import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';

export const fetchProduct = createAsyncThunk(
  'allProducts/fetchAllProducts',
  async()=>{
    const response = await fetch('https://powerful-oasis-75511.herokuapp.com/products')
    .then( res => res.json())
    return response;
  }
)

const productSlice = createSlice({
  name:'Products',
  initialState:{
    allProducts: [],
    displayProducts:[],
    cartProduct:[],
    cartPrice: 0,
    productCategory:'Man',
    isLoading: true,
  },
  reducers: {
    setDisplayProduct : (state,action)=>{
      if(state.allProducts.length > 0){
        const categoryProducts = state.allProducts.filter( p => p.catagory === state.productCategory)
        state.displayProducts = categoryProducts;
      }
    },
    deleteFromCart:(state,action)=>{
     const newCart = state.cartProduct.filter(pd=>pd._id !== action.payload._id)
     state.cartProduct = newCart;
    },
    increaseProductQuantity: (state,action)=>{
      let newCart = []
      state.cartProduct.forEach(pd=>{
        if(pd._id === action.payload._id){
          const newQuantity = action.payload.quantity + 1;
          let product = {...action.payload}
          product.quantity = newQuantity;
          newCart.push(product)
        }
        else{
          newCart.push(pd)
        }
      })
      state.cartProduct = newCart;
      
    },
    decreaseProductQuantity: (state,action)=>{
      let newCart = []
      state.cartProduct.forEach(pd=>{
        if(pd._id === action.payload._id){
          const newQuantity = action.payload.quantity - 1;
          let product = {...action.payload}
          product.quantity = newQuantity;
          newCart.push(product)
        }
        else{
          newCart.push(pd)
        }
      })
      state.cartProduct = newCart;
      
    },
    setCartPrice: (state,action)=>{
      if(state.cartProduct.length>0){
        let totalPrice = 0;
        state.cartProduct.forEach(pd=>{
          totalPrice += parseInt(pd.price)*pd.quantity;
        })
        state.cartPrice = totalPrice;
      }
    },
    setProductsCategory: (state,action)=>{
      state.productCategory = action.payload;
      const categoryProducts = state.allProducts.filter( p => p.catagory === state.productCategory)
      state.displayProducts = categoryProducts;
    },
    setProductToCart:(state,action)=>{
      let exist = []
      if(state.cartProduct.length > 0){
        const existProduct =  state.cartProduct.find( pd=>pd._id === action.payload._id);
        exist.push(existProduct)
        if(!existProduct){
          exist = [];
        }
      }
      if(exist.length !== 0){
        alert(`
        This product already in your cart.
        You can increase the quantity from cart page !`)
      }
      else{
        state.cartProduct.push({...action.payload, quantity: 1})
      }
    }

  },
  extraReducers: ( builder ) =>{
    builder.addCase(fetchProduct.fulfilled,(state, action)=>{
      state.allProducts = action.payload;
      state.isLoading = false;
    })
    
    
  }
})
export const { setDisplayProduct, setProductsCategory, setProductToCart, setCartPrice, increaseProductQuantity, decreaseProductQuantity, deleteFromCart } = productSlice.actions;

export default productSlice.reducer;