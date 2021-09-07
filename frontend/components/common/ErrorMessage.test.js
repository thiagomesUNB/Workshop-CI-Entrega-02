import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import ErrorMessage from './ErrorMessage';

it('should render ErrorMessage', () => {
  const { getByText } = render(<ErrorMessage message="test" />);
  expect(getByText('test')).toBeInTheDocument();
});