import { configureStore } from '@reduxjs/toolkit';
import products from '../features/counter/counterSlice';
export const store = configureStore({
  reducer: {
    products: products,
  }
});
