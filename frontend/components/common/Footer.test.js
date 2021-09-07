import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import Footer from './Footer';

it('should render Footer', () => {
  const { getByText } = render(<Footer />);
  expect(getByText('Thinkster')).toBeInTheDocument();
});