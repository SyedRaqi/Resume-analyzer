import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

const isGitHubActions = process.env.GITHUB_ACTIONS === 'true';

export default defineConfig({
	base: isGitHubActions ? "/Resume-analyzer/" : "/",
	plugins: [react()],
	server: { host: '127.0.0.1', port: 5173, strictPort: true },
});
