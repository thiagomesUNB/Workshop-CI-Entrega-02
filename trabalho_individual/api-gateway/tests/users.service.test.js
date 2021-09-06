import { UsersService } from '../src/adapters/UsersService';

test('createUser()', () => {
    expect(UsersService.createUser({})).toBe(3);
});
