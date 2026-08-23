export interface GymCamClientOptions {
  apiKey?: string;
  baseUrl?: string;
  sandbox?: boolean;
}

export class GymCamClient {
  constructor(options?: GymCamClientOptions);
  apiKey?: string;
  baseUrl: string;
  sandbox: boolean;
  status(): Promise<any>;
  summary(gymId?: string): Promise<any>;
  trainerAttendance(trainer: string, period?: string): Promise<any>;
  classPerformance(limit?: number): Promise<any>;
  revenueInsights(): Promise<any>;
}

export const DEFAULT_BASE: string;
