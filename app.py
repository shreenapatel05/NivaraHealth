import { useState } from 'react';
import { Eye, EyeOff, Lock, Mail, ShieldCheck, User } from 'lucide-react';
import { Button } from './ui/button';
import { Input } from './ui/input';
import { Label } from './ui/label';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from './ui/select';
import { Checkbox } from './ui/checkbox';

export function LoginForm() {
  const [showPassword, setShowPassword] = useState(false);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [role, setRole] = useState('');
  const [rememberMe, setRememberMe] = useState(false);
  const [errors, setErrors] = useState<{ email?: string; password?: string; role?: string }>({});

  const handleLogin = (e: React.FormEvent) => {
    e.preventDefault();
    const newErrors: { email?: string; password?: string; role?: string } = {};

    if (!email) {
      newErrors.email = 'Email is required';
    } else if (!/\S+@\S+\.\S+/.test(email)) {
      newErrors.email = 'Please enter a valid email';
    }

    if (!password) {
      newErrors.password = 'Password is required';
    } else if (password.length < 8) {
      newErrors.password = 'Password must be at least 8 characters';
    }

    if (!role) {
      newErrors.role = 'Please select your role';
    }

    setErrors(newErrors);

    if (Object.keys(newErrors).length === 0) {
      // Simulate login
      console.log('Login attempt:', { email, role, rememberMe });
    }
  };

  return (
    <div className="w-full max-w-md p-8 bg-white rounded-2xl shadow-xl">
      {/* Logo */}
      <div className="flex items-center justify-center mb-6">
        <div className="flex items-center gap-2">
          <div className="w-10 h-10 bg-gradient-to-br from-[#2F80ED] to-[#27AE60] rounded-lg flex items-center justify-center">
            <ShieldCheck className="w-6 h-6 text-white" />
          </div>
          <div>
            <h1 className="text-2xl font-bold text-gray-900">NivaraHealth</h1>
            <p className="text-xs text-gray-500">Healthcare Management</p>
          </div>
        </div>
      </div>

      {/* Title */}
      <div className="text-center mb-8">
        <div className="flex items-center justify-center gap-2 mb-2">
          <Lock className="w-5 h-5 text-[#2F80ED]" />
          <h2 className="text-xl font-semibold text-gray-900">Secure Login</h2>
        </div>
        <p className="text-sm text-gray-500">Access your healthcare dashboard</p>
      </div>

      {/* Form */}
      <form onSubmit={handleLogin} className="space-y-5">
        {/* Email Field */}
        <div className="space-y-2">
          <Label htmlFor="email" className="text-gray-700">Email Address</Label>
          <div className="relative">
            <Mail className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
            <Input
              id="email"
              type="email"
              placeholder="doctor@nivarahealth.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className={`pl-10 ${errors.email ? 'border-red-500' : ''}`}
            />
          </div>
          {errors.email && <p className="text-xs text-red-600">{errors.email}</p>}
        </div>

        {/* Password Field */}
        <div className="space-y-2">
          <Label htmlFor="password" className="text-gray-700">Password</Label>
          <div className="relative">
            <Lock className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
            <Input
              id="password"
              type={showPassword ? 'text' : 'password'}
              placeholder="Enter your password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className={`pl-10 pr-10 ${errors.password ? 'border-red-500' : ''}`}
            />
            <button
              type="button"
              onClick={() => setShowPassword(!showPassword)}
              className="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600"
            >
              {showPassword ? <EyeOff className="w-5 h-5" /> : <Eye className="w-5 h-5" />}
            </button>
          </div>
          {errors.password && <p className="text-xs text-red-600">{errors.password}</p>}
        </div>

        {/* Role Dropdown */}
        <div className="space-y-2">
          <Label htmlFor="role" className="text-gray-700">Select Role</Label>
          <div className="relative">
            <User className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400 z-10 pointer-events-none" />
            <Select value={role} onValueChange={setRole}>
              <SelectTrigger className={`pl-10 ${errors.role ? 'border-red-500' : ''}`}>
                <SelectValue placeholder="Choose your role" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="admin">Administrator</SelectItem>
                <SelectItem value="doctor">Doctor</SelectItem>
                <SelectItem value="staff">Staff</SelectItem>
                <SelectItem value="patient">Patient</SelectItem>
              </SelectContent>
            </Select>
          </div>
          {errors.role && <p className="text-xs text-red-600">{errors.role}</p>}
        </div>

        {/* Remember Me & Forgot Password */}
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <Checkbox
              id="remember"
              checked={rememberMe}
              onCheckedChange={(checked) => setRememberMe(checked as boolean)}
            />
            <Label htmlFor="remember" className="text-sm text-gray-600 cursor-pointer">
              Remember me
            </Label>
          </div>
          <a href="#" className="text-sm text-[#2F80ED] hover:text-[#1e5cb3] hover:underline">
            Forgot password?
          </a>
        </div>

        {/* Login Button */}
        <Button
          type="submit"
          className="w-full bg-gradient-to-r from-[#2F80ED] to-[#27AE60] hover:from-[#1e5cb3] hover:to-[#1e8449] text-white"
        >
          <Lock className="w-4 h-4 mr-2" />
          Sign In Securely
        </Button>
      </form>

      {/* Divider */}
      <div className="relative my-6">
        <div className="absolute inset-0 flex items-center">
          <div className="w-full border-t border-gray-200"></div>
        </div>
        <div className="relative flex justify-center text-sm">
          <span className="px-4 bg-white text-gray-500">New to NivaraHealth?</span>
        </div>
      </div>

      {/* Register Link */}
      <div className="text-center">
        <a href="#" className="text-sm text-gray-600 hover:text-[#2F80ED]">
          Don't have an account? <span className="font-semibold text-[#27AE60]">Request Access</span>
        </a>
      </div>
    </div>
  );
}
